
class SchemojiMapping():
    def __init__(self, m, n):
        # schemoji value
        self.m = m
        # scheme value
        self.n = n

# Language tokens
EXP_OPEN = SchemojiMapping('🔴', '(')
EXP_CLOSE = SchemojiMapping('🔵', ')')

# Operators
OP_ADD = SchemojiMapping('➕', '+')
OP_SUB = SchemojiMapping('➖', '-')
OP_MUL = SchemojiMapping('✖️', '*')
OP_DIV = SchemojiMapping('➗', '/')
OP_GT  = SchemojiMapping('>', '>')
OP_LT  = SchemojiMapping('<', '<')
OP_GE  = SchemojiMapping('🌛', '>=')
OP_LE  = SchemojiMapping('🌜', '<=')
OP_EQ  = SchemojiMapping('⚖️', '=')

# standard scheme procedures
SC_ABS      = SchemojiMapping('🆎', 'abs')
SC_BEGIN    = SchemojiMapping('👌', 'begin')
SC_CAR      = SchemojiMapping('🚗', 'car')
SC_DEFINE   = SchemojiMapping('✏️', 'define')
SC_MAP      = SchemojiMapping('🗺️', 'map')
SC_NOT      = SchemojiMapping('❗', 'not')
SC_NULLQ    = SchemojiMapping('❓', 'null?')
SC_PRINT    = SchemojiMapping('🅿️', 'print')
SC_PI       = SchemojiMapping('🥧', 'pi')


master_token_set = {
    EXP_OPEN, EXP_CLOSE,
    OP_ADD, OP_SUB, OP_MUL, OP_DIV, OP_GT, OP_LT, OP_GE, OP_LE, OP_EQ,
    SC_ABS, SC_BEGIN, SC_CAR, SC_DEFINE, SC_MAP, SC_NOT, SC_NULLQ, SC_PRINT, SC_PI
}
