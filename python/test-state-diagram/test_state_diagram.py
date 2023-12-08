from typing import Protocol


class HealthState(Protocol):
    def switch(self, health) -> None:
        ...


class ServingState:
    def switch(self, health) -> None:
        health.state = NotServingState()
        print('not serving')


class NotServingState:
    def switch(self, health) -> None:
        health.state = ServingState()
        print('serving')


class Health:
    def __init__(self) -> None:
        self.state = ServingState()

    def switch(self) -> None:
        self.state.switch(self)

def main() -> None:
    health = Health()
    health.switch()
    health.switch()


#   The State Design Pattern in Python Explained - YouTube https://www.youtube.com/watch?v=5OzLrbk82zY
if __name__ == '__main__':
    main()
