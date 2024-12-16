import os


def print_hi():
    print("""___________ ________  ________ 
\\_   _____//  _____/ /  _____/ 
 |    __)_/   \\  ___/   \\  ___ 
 |        \\    \\_\\  \\    \\_\\  \\
/_______  /\\______  /\\______  /
        \\/        \\/        \\/""")


if __name__ == '__main__':
    print_hi()

    # Helper function for string to boolean conversion
    def str_to_bool(env):
        return str(env).lower() in ('true', '1', 't', 'y', 'yes')

    # Read and convert environment variables
    isTripletsEnabled = str_to_bool(os.getenv('IS_TRIPLETS_ENABLED', 'false'))
    isNodeIteratorEnabled = str_to_bool(os.getenv('IS_NODE_ITERATOR_ENABLED', 'false'))
    isCompactForward = str_to_bool(os.getenv('IS_COMPACT_FORWARD', 'false'))
    isTriestEnabled = str_to_bool(os.getenv('IS_TRIEST_ENABLED', 'false'))
    isDoulionEnabled = str_to_bool(os.getenv('IS_DOULION_ENABLED', 'false'))

    print("\nSpecific Environment Variables:")
    print(f"IS TRIPLETS ENABLED: {isTripletsEnabled}")
    print(f"IS NODE ITERATOR ENABLED: {isNodeIteratorEnabled}")
    print(f"IS COMPACT FORWARD ENABLED: {isCompactForward}")
    print(f"IS TRIEST ENABLED: {isTriestEnabled}")
    print(f"IS DOULION ENABLED: {isDoulionEnabled}")