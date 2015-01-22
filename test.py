import ply.lex as lex
# List of token names.
tokens = (
       'NUMBER',
       'PLUS',
       'MINUS',
       'TIMES',
       'DIVIDE',
       'LPAREN',
       'RPAREN',
)
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
# A regular expression rule with some action code
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)    
	return t
# Define a rule so we can track line numbers
def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# Error handling rule
def t_error(t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()
# Test it out
f=open("abc.txt",'r')
g=open("abcd.txt",'w')
out=f.readlines()
for line in out: 
	#print line
	data=line
	g.write(data.strip()+"\t\t\t\t")
	lexer.input(data)
	while True:
		tok = lexer.token()
        	if not tok: break 
        	g.write(str(tok.type)+" ")
		#print type(tok)
	g.write("\n")
