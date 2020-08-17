from pysparkling.sql.expressions.expressions import Expression, UnaryExpression, \
    NullSafeBinaryOperation, TypeSafeBinaryOperation


class Negate(UnaryExpression):
    def eval(self, row, schema):
        return not self.column.eval(row, schema)

    def __str__(self):
        return "(- {0})".format(self.column)


class Add(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return value1 + value2

    def __str__(self):
        return "({0} + {1})".format(self.arg1, self.arg2)


class Minus(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return value1 - value2

    def __str__(self):
        return "({0} - {1})".format(self.arg1, self.arg2)


class Time(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return value1 * value2

    def __str__(self):
        return "({0} * {1})".format(self.arg1, self.arg2)


class Divide(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return value1 / value2 if value2 != 0 else None

    def __str__(self):
        return "({0} / {1})".format(self.arg1, self.arg2)


class Mod(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return value1 % value2

    def __str__(self):
        return "({0} % {1})".format(self.arg1, self.arg2)


class Pow(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return float(value1 ** value2)

    def __str__(self):
        return "POWER({0}, {1})".format(self.arg1, self.arg2)


class Pmod(NullSafeBinaryOperation):
    def unsafe_operation(self, value1, value2):
        return value1 % value2

    def __str__(self):
        return "pmod({0} % {1})".format(self.arg1, self.arg2)


class Equal(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 == value_2

    def __str__(self):
        return "({0} = {1})".format(self.arg1, self.arg2)


class LessThan(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 < value_2

    def __str__(self):
        return "({0} < {1})".format(self.arg1, self.arg2)


class LessThanOrEqual(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 <= value_2

    def __str__(self):
        return "({0} <= {1})".format(self.arg1, self.arg2)


class GreaterThan(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 > value_2

    def __str__(self):
        return "({0} > {1})".format(self.arg1, self.arg2)


class GreaterThanOrEqual(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 >= value_2

    def __str__(self):
        return "({0} >= {1})".format(self.arg1, self.arg2)


class And(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 and value_2

    def __str__(self):
        return "({0} AND {1})".format(self.arg1, self.arg2)


class Or(TypeSafeBinaryOperation):
    def unsafe_operation(self, value_1, value_2):
        return value_1 or value_2

    def __str__(self):
        return "({0} OR {1})".format(self.arg1, self.arg2)


class Invert(UnaryExpression):
    def eval(self, row, schema):
        value = self.column.eval(row, schema)
        if value is None:
            return None
        return not value

    def __str__(self):
        return "(NOT {0})".format(self.column)


class BitwiseOr(Expression):
    def __init__(self, arg1, arg2):
        super(BitwiseOr, self).__init__(arg1, arg2)
        self.arg1 = arg1
        self.arg2 = arg2

    def eval(self, row, schema):
        return self.arg1.eval(row, schema) | self.arg2.eval(row, schema)

    def __str__(self):
        return "({0} | {1})".format(self.arg1, self.arg2)


class BitwiseAnd(Expression):
    def __init__(self, arg1, arg2):
        super(BitwiseAnd, self).__init__(arg1, arg2)
        self.arg1 = arg1
        self.arg2 = arg2

    def eval(self, row, schema):
        return self.arg1.eval(row, schema) & self.arg2.eval(row, schema)

    def __str__(self):
        return "({0} & {1})".format(self.arg1, self.arg2)


class BitwiseXor(Expression):
    def __init__(self, arg1, arg2):
        super(BitwiseXor, self).__init__(arg1, arg2)
        self.arg1 = arg1
        self.arg2 = arg2

    def eval(self, row, schema):
        return self.arg1.eval(row, schema) ^ self.arg2.eval(row, schema)

    def __str__(self):
        return "({0} ^ {1})".format(self.arg1, self.arg2)
