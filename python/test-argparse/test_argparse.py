import argparse

# https://pymotw.com/2/argparse/


parser = argparse.ArgumentParser(description='test of command line options')

parser.add_argument('-a', action='store_true', default=False)
parser.add_argument('-b', action='store', dest='b')
parser.add_argument('-c', action='store', dest='c', type=int)

opt = parser.parse_args(['-a', '-bval', '-c', '3'])
print 'a {}\tb {}\tc {}'.format(opt.a, opt.b, opt.c)
print '-' * 50


parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action="store_true", default=False)
parser.add_argument('--witharg', action="store", dest="witharg")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

opt = parser.parse_args([ '--noarg', '--witharg', 'val', '--witharg2=3' ])
print 'noarg {}\twitharg {}\twitharg2 {}'.format(opt.noarg, opt.witharg, opt.witharg2)
print '-' * 50


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action='store_true')

try:
  print parser.parse_args(['-a', '-b'])
except:
  pass
print '-' * 50


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# A list command
list_parser = subparsers.add_parser('list', help='List contents')
list_parser.add_argument('dirname', action='store', help='Directory to list')

# A create command
create_parser = subparsers.add_parser('create', help='Create a directory')
create_parser.add_argument('dirname', action='store', help='New directory to create')
create_parser.add_argument('--read-only', default=False, action='store_true',
                           help='Set permissions to prevent writing to the directory',
                           )

# A delete command
delete_parser = subparsers.add_parser('delete', help='Remove a directory')
delete_parser.add_argument('dirname', action='store', help='The directory to remove')
delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
                           help='Remove the contents of the directory, too',
                           )

print parser.parse_args(['list', 'dirname_to_list'])
print parser.parse_args(['create', 'dirname_to_create', '--read-only'])
print parser.parse_args(['delete', 'dirname_to_delete', '-r'])
try:
  print parser.parse_args(['list', 'dirname', 'create', 'dirname'])
except:
  pass
