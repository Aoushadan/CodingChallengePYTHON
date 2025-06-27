import configparser

def get_property_string(filename):
    try:
        config = configparser.ConfigParser()
        read_files = config.read(filename)
        if not read_files:
            raise FileNotFoundError(f"Property file '{filename}' not found or empty.")

        if 'database' not in config:
            raise KeyError("Missing 'database' section in property file.")

        db_config = config['database']

        return {
            'server': db_config.get('server', ''),
            'database': db_config.get('database', ''),
            'username': db_config.get('username', ''),  # can be empty if trusted connection
            'password': db_config.get('password', '')   # can be empty if trusted connection
        }

    except Exception as e:
        print(f"[PropertyUtil Error] Failed to read properties: {e}")
        return None
