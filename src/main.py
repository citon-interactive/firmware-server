from src.core.state_machine import FirmwareUpdateStateMachine
import time

def main():
    """Main entry point for the firmware server."""
    print("Starting Firmware Update Server...")
    
    # Create and start the state machine
    fsm = FirmwareUpdateStateMachine()
    
    # Print initial state
    print(f"Initial state: {fsm.current_state}")
    
    # Demo: Simulate state transitions
    # In a real implementation, these transitions would be triggered
    # by actual events (network connection success/failure, API responses, etc.)
    
    try:
        # Simulate authentication failure -> go to configuring
        print("\n--- Simulating authentication failure ---")
        fsm.auth_failed()
        print(f"Current state: {fsm.current_state}")
        
        time.sleep(1)
        
        # Simulate configuration success -> back to authenticating
        print("\n--- Simulating configuration success ---")
        fsm.config_success()
        print(f"Current state: {fsm.current_state}")
        
        time.sleep(1)
        
        # Simulate authentication success -> go to API authenticating
        print("\n--- Simulating authentication success ---")
        fsm.auth_success()
        print(f"Current state: {fsm.current_state}")
        
        time.sleep(1)
        
        # Simulate API authentication success -> go to serving
        print("\n--- Simulating API authentication success ---")
        fsm.api_auth_success()
        print(f"Current state: {fsm.current_state}")
        
        print("\n--- Firmware server is now serving! ---")
        
    except Exception as e:
        print(f"Error in state machine: {e}")

if __name__ == "__main__":
    main()