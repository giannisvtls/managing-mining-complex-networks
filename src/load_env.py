import os
from pathlib import Path

def load_env():
    """
    Load environment variables from .env file
    Returns a dict of the loaded variables
    """
    env_path = Path(__file__).parent.parent / '.env'
    
    if not env_path.exists():
        print(f"Warning: .env file not found at {env_path}")
        return {}
    
    env_vars = {}
    
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
                
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip("'").strip('"')
                
                os.environ[key] = value
                env_vars[key] = value
    
    return env_vars

if __name__ == '__main__':
    env_vars = load_env()
    print("\nLoaded environment variables:")
    for key, value in env_vars.items():
        print(f"{key}: {value}")
