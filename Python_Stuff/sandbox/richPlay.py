import rich as rich
from rich.traceback import install
install(show_locals=True)

rich.print("Hello, World")

# test traceback install

# try:
#     bar(1)
# except Exception as e:
#     rich.print_exception()

from rich.console import Console
from rich.text import Text

console = Console()
text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)
console.print(text)

# With Logging:
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")

# Print JSON to console
console.print_json('[false, true, null, "foo"]')

from rich.json import JSON
console.log(JSON('["foo", "bar"]'))
