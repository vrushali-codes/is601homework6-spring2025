from calculator.calculation_history import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable
# from calculator.commands import CommandHandler
# from calculator.commands.greet import GreetCommand
# from calculator.commands.exit import ExitCommand
# from calculator.commands.add import AddCommand

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)

# # Move App outside of Calculator
# class App:
#     def __init__(self):  # Constructor
#         self.command_handler = CommandHandler()

#     def start(self):
#         # Register commands here
#         self.command_handler.register_command("greet", GreetCommand())
#         # self.command_handler.register_command("goodbye", GoodbyeCommand())
#         self.command_handler.register_command("exit", ExitCommand())
#         self.command_handler.register_command("add", AddCommand())
#         # self.command_handler.register_command("menu", MenuCommand())
#         # self.command_handler.register_command("discord", DiscordCommand())

#         print("Type 'exit' to exit.")
#         while True:  # REPL (Read, Evaluate, Print, Loop)
#             self.command_handler.execute_command(input(">>> ").strip())        