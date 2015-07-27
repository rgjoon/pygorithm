import sys, random

def parse(v):
	try:
		i = int(v)
	except ValueError:
		i = 0

	return i

def main(argv):
  if len(argv) != 4:
    print 'Usage: python %s <start number> <end number> <total count>' % argv[0]
  else:
    s = parse(argv[1])
    e = parse(argv[2])
    c = parse(argv[3])

    for n in xrange(c):
    	print "%d" % random.randrange(s, e + 1)

if __name__ == '__main__':
  main(sys.argv)

