# EOF(End-Of-File)
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
	# token: strings with an assigned and thus identified meaning
	def __init__(self, type, value):
		self.type = type  # type of token: INTEGER/PLUS/MINUS/EOF
		self.value = value  # value of token: 0 .. 9, '+' or None

	def __str__(self):
		""" String representation of the class instance.

		Examples:
				Token(Integer, 3)
				Token(PLUS, '+')
		"""

		return 'Token({type}, {value})'.format(
			type = self.type,
			value = repr(self.value)
			)

	def __repr__(self):
		return self.__str__()

class Interpreter(object):
	def __init__(self, text):
		self.text = text  # input string, e.g. "1+2"
		self.pos = 0  # self.pos is the index of self.text.
		self.current_token = None

	def error(self):
		raise Exception('Error parsing input.')

	def get_next_token(self):
		""" lexical analyzer(scanner)

		converting a sequence of charachters into a sequence of tokens

		"""

		text = self.text

		if self.pos > len(text) - 1:
			return Token(EOF, None)
			

		current_char = text[self.pos]
		
		if current_char.isdigit(): # check if current_char is a digit(number)
			token = Token(INTEGER, int(current_char))
			self.pos += 1
			return token

		if current_char == '+':
			token = Token(PLUS, current_char)
			self.pos += 1
			return token

		self.error()

	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def expr(self):
		""" expr: find the structure INTEGER->PLUS->INTEGER """
		self.current_token = self.get_next_token()

		left = self.current_token
		self.eat(INTEGER)

		op = self.current_token
		self.eat(PLUS)

		right = self.current_token
		self.eat(INTEGER)

		result = left.value + right.value
		return result


def main():
		while True:
			try:
				text = input('calc> ') # 'input' under python3, 'raw_input' under python2
			except EOFError:
				break
			if not text:
				continue
			interpreter = Interpreter(text)
			result = interpreter.expr()
			print(result)

if __name__ == '__main__':
		main()










