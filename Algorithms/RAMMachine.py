def _is_int(val):
	if not isinstance(val, int):
		raise ValueError('type \'{}\' was given'.format(type(val)))


class _Command:

	def __init__(self, label):
		self.__label = label
		
	@property
	def label(self):
		return self.__label


class LOAD(_Command):

	def __init__(self, value, spec=None, label=None):
		super(LOAD, self).__init__(label)
		_is_int(value)
		self.__value = value
		self.__spec = spec

	@property
	def value(self):
		return self.__value

	@property
	def spec(self):
		return self.__spec


class READ(_Command):
	
	def __init__(self, register, hint='Enter integer value > ', label=None):
		super(READ, self).__init__(label)
		_is_int(register)
		self.__register = register
		self.__hint = hint
		
	def read(self):
		return int(input(self.__hint))
	
	@property
	def register(self):
		return self.__register


class STORE(_Command):
	
	def __init__(self, register, label=None):
		super(STORE, self).__init__(label)
		_is_int(register)
		self.__register = register

	@property
	def register(self):
		return self.__register


class ADD(_Command):
	
	def __init__(self, value, spec=None, label=None):
		super(ADD, self).__init__(label)
		_is_int(value)
		self.__value = value
		self.__spec = spec

	@property
	def value(self):
		return self.__value

	@property
	def spec(self):
		return self.__spec


class SUB(_Command):
	
	def __init__(self, value, spec=None, label=None):
		super(SUB, self).__init__(label)
		_is_int(value)
		self.__value = value
		self.__spec = spec

	@property
	def value(self):
		return self.__value

	@property
	def spec(self):
		return self.__spec


class DIV(_Command):
	
	def __init__(self, value, spec=None, label=None):
		super(DIV, self).__init__(label)
		self.__value = value
		self.__spec = spec

	@property
	def value(self):
		return self.__value

	@property
	def spec(self):
		return self.__spec


class MULT(_Command):
	
	def __init__(self, value, spec=None, label=None):
		super(MULT, self).__init__(label)
		_is_int(value)
		self.__value = value
		self.__spec = spec

	@property
	def value(self):
		return self.__value

	@property
	def spec(self):
		return self.__spec


class WRITE(_Command):
	
	def __init__(self, register, label=None):
		super(WRITE, self).__init__(label)
		_is_int(register)
		self.__register = register

	@property
	def register(self):
		return self.__register


class HALT(_Command):
	
	def __init__(self, label=None):
		super(HALT, self).__init__(label)


class JUMP(_Command):
	
	def __init__(self, target, label=None):
		super(JUMP, self).__init__(label)
		self.__target_label = target

	@property
	def target(self):
		return self.__target_label


class JGTZ(_Command):
	
	def __init__(self, target, label=None):
		super(JGTZ, self).__init__(label)
		self.__target_label = target

	@property
	def target(self):
		return self.__target_label


class JZERO(_Command):
	
	def __init__(self, target, label=None):
		super(JZERO, self).__init__(label)
		self.__target_label = target

	@property
	def target(self):
		return self.__target_label


class RAMMachine:
	_AVAILABLE_COMMANDS = [LOAD, READ, STORE, ADD, SUB, DIV, MULT, WRITE, HALT, JUMP, JGTZ, JZERO]
	
	def __init__(self, commands):
		self._validate(commands)
		self.__commands = commands
		self.__registers = []
		self.__read_val = None
	
	def _validate(self, commands):
		for command in commands:
			if not isinstance(command, _Command) or type(command) not in self._AVAILABLE_COMMANDS:
				raise Exception("unknown command received: '{}'".format(type(command)))
		if not any(isinstance(command, HALT) for command in commands):
			raise Exception("program has no 'HALT' command")
	
	def _store_reg(self, reg_num):
		if reg_num < 1:
			raise IndexError("invalid register number received")
		if reg_num >= len(self.__registers):
			while len(self.__registers) != reg_num + 1:
				self.__registers.append(None)
		self.__registers[reg_num] = self._adder
	
	def _get_reg_data(self, reg_num):
		if reg_num >= len(self.__registers):
			raise IndexError('register does not exist')
		return self.__registers[reg_num]
	
	def _get_command_id_by_label(self, target, curr_i):
		if target is not None:
			for i in range(len(self.__commands)):
				if self.__commands[i].label == target:
					return i
			else:
				raise Exception("unknown label received")
		return curr_i + 1
	
	def _set_adder(self, val):
		if len(self.__registers) < 1:
			self.__registers.append(val)
		self.__registers[0] = val
	
	def exec(self):
		i = 0
		while True:
			next_cmd = self._exec_command(self.__commands[i])
			if next_cmd is HALT:
				break
			i = self._get_command_id_by_label(next_cmd, i)
	
	def _exec_command(self, cmd):
		if isinstance(cmd, LOAD):
			self._load(cmd.value, cmd.spec)
		elif isinstance(cmd, READ):
			self._load(cmd.read(), '=')
			self._store_reg(cmd.register)
		elif isinstance(cmd, STORE):
			self._store(cmd.register)
		elif isinstance(cmd, ADD):
			self._add(cmd.value, cmd.spec)
		elif isinstance(cmd, SUB):
			self._sub(cmd.value, cmd.spec)
		elif isinstance(cmd, DIV):
			self._div(cmd.value, cmd.spec)
		elif isinstance(cmd, MULT):
			self._mult(cmd.value, cmd.spec)
		elif isinstance(cmd, WRITE):
			print(self.__registers[cmd.register])
		elif isinstance(cmd, HALT):
			return HALT
		elif isinstance(cmd, JUMP):
			return cmd.target
		elif isinstance(cmd, JGTZ):
			if self._adder > 0:
				return cmd.target
		elif isinstance(cmd, JZERO):
			if self._adder == 0:
				return cmd.target
		else:
			raise Exception('invalid command was given')
		return None
	
	def _get_val_for_operation(self, val, spec=None):
		if spec == '=':
			res = val
		elif spec == '*':
			res = self._get_reg_data(self._get_reg_data(val))
		else:
			res = self._get_reg_data(val)
		return res
	
	@property
	def _adder(self):
		return self.__registers[0]
	
	def _load(self, val, spec=None):
		if spec:
			if spec == "=":
				self._set_adder(val)
			elif spec == "*":
				self._set_adder(self.__registers[self.__registers[val]])
		else:
			self._set_adder(self.__registers[val])
	
	def _store(self, reg):
		self._store_reg(reg)
	
	def _sub(self, val, spec=None):
		self._set_adder(self._adder - self._get_val_for_operation(val, spec))
	
	def _add(self, val, spec=None):
		self._set_adder(self._adder + self._get_val_for_operation(val, spec))
	
	def _div(self, val, spec=None):
		self._set_adder(self._adder / self._get_val_for_operation(val, spec))
	
	def _mult(self, val, spec=None):
		self._set_adder(self._adder * self._get_val_for_operation(val, spec))
