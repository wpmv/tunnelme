"""Main tunnel_utils code location.

This is a useful location for functions called by script endpoints.
"""
import logging
import logging.config
import click
from tunnel_utils.tunnels.devnull_workpc.ssh import DevnullWorkPCTunnel
from tunnel_utils.logging import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


@click.command()
@click.option('-h', '--hostname', required=True, type=click.types.STRING)
@click.option('-p', '--password', required=True, type=click.types.STRING)
@click.option('-c', '--grid-card', required=True, type=click.types.Path(exists=True))
@click.option('--interact/--no-interact', default=True)
def main(hostname, password, grid_card, interact):
    """
    Primary entry point for script command.
    """
    ssh_tunnel = DevnullWorkPCTunnel(
        hostname=hostname,
        target_password=password,
        grid_filepath=grid_card,
    ).start_tunnel()
    if interact:
        logger.info("Opening interactive session...")
        ssh_tunnel.interact()
