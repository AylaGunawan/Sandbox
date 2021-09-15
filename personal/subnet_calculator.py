"""
Personal Project - 15/09/2021
Subnet Calculator
"""


def main():
    """Subnet calculator program for IPv4."""
    # address_ip_binary = "11001000.11001000.10001010.11011110"
    # address_mask_binary = "11111111.11111111.11111111.00000000"

    address_ip_binary = get_valid_binary_address("IP Address")
    address_mask_binary = get_valid_binary_address("Mask Address")

    address_ip_decimal = convert_binary_to_decimal(address_ip_binary)
    address_mask_decimal = convert_binary_to_decimal(address_mask_binary)
    address_subnet_binary = calculate_subnet_binary(address_ip_binary, address_mask_binary)
    address_subnet_decimal = convert_binary_to_decimal(address_subnet_binary)

    print(f"""
    IP Address
    ----------
    Binary: {address_ip_binary}
    Decimal: {address_ip_decimal}
    
    Mask Address
    ------------
    Binary: {address_mask_binary}
    Decimal: {address_mask_decimal}
    
    Subnet Address
    --------------
    Binary: {address_subnet_binary}
    Decimal: {address_subnet_decimal}
    """)


def convert_binary_to_decimal(binary):
    """Convert binary address into decimal address."""
    binary_octets = binary.split(".")
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    decimal = ".".join(decimal_octets)
    return decimal


def convert_decimal_to_binary(decimal):  # currently unused
    """Convert decimal address into binary address."""
    decimal_octets = decimal.split(".")
    binary_octets = [str(bin(octet)) for octet in decimal_octets]
    binary = ".".join(binary_octets)
    return binary


def calculate_subnet_binary(ip, mask):
    """Calculate subnet in binary using AND logic between IP and mask address."""
    subnet_bits = []
    for index, bit in enumerate(ip):
        if bit == ".":
            subnet_bits.append(".")
        elif bit == "1" and ip[index] == mask[index]:
            subnet_bits.append("1")
        else:
            subnet_bits.append("0")
    subnet = "".join(subnet_bits)
    return subnet


def get_valid_binary_address(prompt):
    """Get valid binary address."""
    octets = []
    for i in range(4):  # 4 = number of octets in IPv4
        octet = input(prompt + f" Octet {i + 1} (binary): ")
        while len(octet) != 8 or not octet.isdigit():  # 8 = length of octet
            print("Invalid octet")
            octet = input(prompt + f" Octet {i + 1} (binary): ")
        octets.append(octet)
    address = ".".join(octets)
    return address


main()
