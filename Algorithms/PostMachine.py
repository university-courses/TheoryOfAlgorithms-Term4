class PostMachine:

	def __init__(self, commands):
		self.__available_commands = [
			'->',  # move the caret to the right for 1 cell
			'<-',  # move the caret to the left for 1 cell
			'V',   # replace 0 into 1
			'E',   # replace 1 into 0
			'?',   # if-else statement ['?', i, j]: if cell is 0 than run command 'a', else - run command 'b'
			'!'	   # terminates program
		]
		self.__validate_commands(commands)
		self.__commands = commands
		self.__caret_position = 0
		self.__operations_count = 0

	def __validate_commands(self, commands):
		has_terminal_command = False
		for command in commands:
			if command[0] not in self.__available_commands:
				raise KeyError('command "{}" does not exist'.format(command[0]))
			if command[0] == '!':
				has_terminal_command = True
		if not has_terminal_command:
			raise KeyError('machine does not contain terminal command')

	def __execute_command(self, command, string):
		new = list(string)
		current_command = command[0]
		next_command = command[1]
		if current_command == '->':
			if self.__caret_position < len(string):
				self.__caret_position += 1
		elif current_command == '<-':
			if self.__caret_position >= 0:
				self.__caret_position -= 1
		elif current_command == 'V':
			new[self.__caret_position] = '1'
		elif current_command == 'E':
			new[self.__caret_position] = '0'
		elif current_command == '?':
			if new[self.__caret_position] == '1':
				next_command = command[2]
		elif current_command == '!':
			return string
		else:
			raise KeyError('command "{}" does not exist'.format(command[0]))
		self.__operations_count += 1
		return self.__execute_command(self.__commands[next_command - 1], ''.join(new))

	def transform_line(self, input_line, start_pos=0, prefix=0):
		if prefix < 0:
			prefix = 0
		if start_pos < 0:
			start_pos = 0
		self.__caret_position = start_pos + prefix
		string = ('0' * prefix) + input_line + ('0' * prefix)
		return self.__execute_command(self.__commands[0], string)

	@property
	def operations_ran(self):
		return self.__operations_count
