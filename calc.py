# EOF(End-Of-File)
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
	# token: strings with an assigned and thus identified meaning
	def __init__(self, type, value):
		self.type = type  # type of token: INTEGER/PLUS/MINUS/EOF
		self.value = value  # value of token: non-negative integer value, '+','-' or None

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
		self.current_char = self.text[self.pos]

	def error(self):
		raise Exception('Error parsing input.')

	def advance(self):
		""" Advance the 'pos' pointer and set the 'current_char' variable """
		self.pos += 1
		if self.pos > len(self.text) - 1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	def skip_whitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.advance()

	def integer(self):
		""" Return a multidigit integer consumed from the input """
		result = ''
		while self.current_char is not None and self.current_char.isdigit():
			result += self.current_char
			self.advance()
		return int(result)


	def get_next_token(self):
		""" lexical analyzer(scanner)

		Converts a sequence of charachters into a sequence of tokens

		"""

		while self.current_char is not None:

			if self.current_char.isspace():
				self.skip_whitespace()
				continue

			if self.current_char.isdigit():
				return Token(INTEGER, self.integer())

			if self.current_char == '+':
				self.advance()
				return Token(PLUS, '+')

			if self.current_char == '-':
				self.advance()
				return Token(MINUS, '-')
			

			self.error()

		return Token(EOF, None)

	def eat(self, token_type):
		"""

		Compare the current token type with the passed token type.
		If the match, then 'eat' the current token and assign the next token to the self.current_token,
		otherwise raise an exception.
		
		"""

		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def expr(self):
		""" 
		expr: find the structure INTEGER->PLUS->INTEGER 
		                         INTEGER->MINUS->INTEGER
		"""
		self.current_token = self.get_next_token() # Set current token to the first token taken from the input

		# Expect the current token to be an integer
		left = self.current_token
		self.eat(INTEGER)

		# Expect the current token to be either '+' or "-"
		op = self.current_token
		if op.type == PLUS:
			self.eat(PLUS)
		else:
			self.eat(MINUS)

		right = self.current_token
		self.eat(INTEGER)

		if op.type == PLUS:
			result = left.value + right.value
		else:
			result = left.value - right.value
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










