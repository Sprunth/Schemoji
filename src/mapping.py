
class SchemojiMapping():
    def __init__(self, m, n):
        # schemoji value
        self.m = m
        # scheme value
        self.n = n

# Language tokens
EXP_OPEN = SchemojiMapping('🔸', '(')
EXP_CLOSE = SchemojiMapping('🔹', ')')
EXP_OPENCLOSE_ALT = {
    0: '0️⃣',
    1: '1️⃣',
    2: '2️⃣',
    3: '3️⃣',
    4: '4️⃣',
    5: '5️⃣',
    6: '6️⃣',
    7: '7️⃣',
    8: '8️⃣',
    9: '9️⃣',
    10: '🔟',
}
EXP_CLOSE_ALT_IDENTIFIER = '\u2009'  # to identify between open and close for ALT

# Operators
OP_ADD = SchemojiMapping('🇨🇭', '+')
OP_SUB = SchemojiMapping('➖', '-')
OP_MUL = SchemojiMapping('🇽', '*')
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
SC_CDR      = SchemojiMapping('🖖', 'cdr')
SC_CONS     = SchemojiMapping('🔀', 'cons')
SC_DEFINE   = SchemojiMapping('✏️', 'define')
SC_IF       = SchemojiMapping('☯️', 'if')
SC_EQUALQ   = SchemojiMapping('❔', 'equal?')
SC_LAMBDA   = SchemojiMapping('🐏', 'lambda')
SC_LIST     = SchemojiMapping('♒', 'list')
SC_MAP      = SchemojiMapping('🗺️', 'map')
SC_NOT      = SchemojiMapping('❗', 'not')
SC_NULLQ    = SchemojiMapping('❓', 'null?')
SC_PRINT    = SchemojiMapping('🙈', 'print')
SC_PI       = SchemojiMapping('🥧', 'pi')
SC_QUOTE    = SchemojiMapping('💬', 'quote')

master_token_set = [
    EXP_OPEN, EXP_CLOSE,
    OP_ADD, OP_SUB, OP_MUL, OP_DIV, OP_GT, OP_LT, OP_GE, OP_LE, OP_EQ,
    SC_ABS, SC_BEGIN, SC_CAR, SC_CDR, SC_CONS, SC_DEFINE, SC_EQUALQ, SC_IF, SC_LAMBDA, SC_LIST,
    SC_MAP, SC_NOT, SC_NULLQ, SC_PRINT, SC_PI, SC_QUOTE
]
