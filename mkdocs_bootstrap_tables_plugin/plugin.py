import os
import sys
import re
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class BootstrapTablesPlugin(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_post_page(self, output_content, page, config):
        output_content = re.sub(r"<table>", "<table class=\"table\">", output_content)
        output_content = re.sub(r"<th>", "<th scope=\"col\">", output_content)
        return output_content

