from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, registers):
        self.registers = registers
        self.index = 0

    def __next__(self):
        try:
            current_value = self.registers[self.index]

        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return current_value
