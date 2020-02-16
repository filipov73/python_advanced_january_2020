import os

while True:
    inp_line = input()
    
    if inp_line == 'End':
        break

    cmd, *args = inp_line.split( '-' )

    if cmd == 'Create':
        f_name, *data = args
        f_handle = open( f_name, 'w' )
        f_handle.write( '' )
        f_handle.close()
    elif cmd == 'Add':
        f_name, *data = args
        try:
            f_handle = open( f_name, 'a' )
        except:
            f_handle = open( f_name, 'w' )
        f_handle.write( data[0] + "\n" )
        f_handle.close()
    elif cmd == 'Replace':
        f_name, *data = args
        try:
            f_handle = open( f_name, 'r' )
            tmp      = open( 'tmp',  'w' )

            for line in f_handle:
                find, repl = data
                words = line.strip().split( " " )
                for i in range( len( words ) ):
                    wrd = words[ i ]
                    if wrd == find:
                        words[ i ] = repl
                
                tmp.write( " ".join( words ) + "\n" )
            
            f_handle.close()
            tmp.close()
            os.remove( f_name )

            tmp      = open( './tmp',  'r' )
            f_handle = open( f_name, 'w' )
            for line in tmp:
                f_handle.write( line.strip() + "\n" )
            
            tmp.close()
            f_handle.close()
            os.remove( './tmp' )
        except:
            print( "An error occured" )
    elif cmd == 'Delete':
        f_name, *data = args
        try:
            os.remove( "./" + f_name )
        except:
            print( "An error occured" )