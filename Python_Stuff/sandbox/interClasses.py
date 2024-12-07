from rich.traceback import install
install(show_locals=True)

from classesPlay import Address

address = Address.Address("123 Main St", "Anytown", "12345")
print(address.display_address())
