import pstats

def main():
    '''open a cprofile report'''
    p = pstats.Stats('profile_1_out')
    p.print_stats()

if __name__ == '__main__':
    main()
