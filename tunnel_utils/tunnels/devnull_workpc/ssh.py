import time
import random
import logging
import pexpect
from tunnel_utils.tunnels.ssh import BaseSSHTunnel
from tunnel_utils.grid_card import GridCard
from tunnel_utils.tunnels.devnull_workpc import parsers

logger = logging.getLogger(__name__)


class DevnullWorkPCTunnel(BaseSSHTunnel):
    def __init__(self, hostname, target_password, grid_filepath, jumper_password=None, success_prompt=None):
        self.hostname = hostname
        self.target_password = target_password
        self.jumper_password = jumper_password or target_password
        self.success_prompt = success_prompt or "$"
        self.grid_card = GridCard(grid_filepath)

    def start_tunnel(self):
        logger.info("Initiating tunnel...")
        tunnel_command = self.get_tunnel_command()
        logger.info("Using tunnel command: '{}'".format(tunnel_command))
        ssh_tunnel = pexpect.spawn(tunnel_command)
        ssh_tunnel.expect("assword:")
        time.sleep(random.uniform(0.1, 1.0))
        logger.info("Authenticating with devnull...")
        ssh_tunnel.sendline(self.jumper_password)
        ssh_tunnel.expect(
            "using a card with serial number {}.".format(self.grid_card.get_serial())
        )
        challenge_message = ssh_tunnel.before.decode("utf-8").strip()
        logger.info("Received challenge: {}".format(challenge_message))
        challenge_response = self.get_challenge_answer(challenge_message)
        time.sleep(random.uniform(3.0, 7.0))
        logger.info("Sending challenge response: '{}'".format(challenge_response))
        ssh_tunnel.sendline(challenge_response)
        ssh_tunnel.expect("assword:")
        time.sleep(random.uniform(0.1, 1.0))
        logger.info("Authenticating with {}...".format(self.hostname))
        ssh_tunnel.sendline(self.target_password)
        ssh_tunnel.expect(self.success_prompt)
        logger.info("Successfully connected!")
        return ssh_tunnel

    def get_tunnel_command(self):
        return "ssh {}".format(self.hostname)

    def get_challenge_answer(self, challenge_message):
        coordinates = parsers.extract_coordinates(challenge_message)
        answer = []
        for coord in coordinates:
            answer.append(self.grid_card.get_coordinate(coord[0], coord[1]))
        return "".join(answer)
