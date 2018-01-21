def help_(DecOrEn,OutOrIn):
    about_me = '''
        Hi!!, My name is {0}Khiem Nguyen{1} aka {2}TopKeingt{1}. 
        
        I'm a student in Malden High School and love to code.I trying to learn as many programming
        languages as possible.
        
        If you found some bug, please let me know because not everything is perfect by pulling request at 
        my github link {3}{4}https://github.com/TopKeingt/EnciphDeWord{1} or straight to me 
        {3}{4}ppkhiemnguyen{5}@{1}{3}{4}gmail.com{1}    
    '''
    options =  '''
      {0}1{1}.{2} Encrypt{1}
      {0}2{1}.{2} Decrypt{1} 
      {0}3{1}.{2} Help 
      {0}4{1}.{2} About me{1}
      {0}5{1}.{2} Banner {1} 
      {0}6{1}.{2} Exit{1} 
      '''
    help_outside_encrypt = '''
    {0}help{1}            -- Display this help message 
    {0}show options{1}    -- Show encryption types
    {0}use [numbers]{1}   -- Use encryption types
    {0}back{1}            -- back to main 
    '''
    
    help_inside_encrypt = '''
    {0}help{1}                                -- Display this help message
    {0}profile{1}                             -- Display profile of this encryption
    {0}show info{1}                           -- Show info box of your encrypter
    {0}SET (message/key) [string/number]{1}   -- set message or key to your given string or number
    {0}message{1}                             -- A wizard type if you don't want to use SET command
    {0}key{1}                                 -- A wizard type if you don't want to use SET command
    {0}execute{1}                             -- Run the encryption
    {0}back{1}                                -- back to encrypt choices 
    '''
    help_inside_decrypt = '''
    {0}help{1}                                -- Display this help message
    {0}profile{1}                             -- Display profile of this encryption
    {0}show info{1}                           -- Show info box of your decrypter
    {0}SET (message/key) [string/number]{1}   -- set encrypted message or key to your given string or number
    {0}message{1}                             -- A wizard type if you don't want to use SET command
    {0}key{1}                                 -- A wizard type if you don't want to use SET command
    {0}execute{1}                             -- Run the decryption
    {0}back{1}                                -- back to encrypt choices 
    '''
    help_outside_decrypt = '''
    {0}help{1}             -- Display this help message 
    {0}show options{1}     -- Show decryption types
    {0}use [numbers]{1}    -- Use decryption types
    {0}back{1}             -- back to main 
    '''
    msg_helper = "Message that gonna {}"
    key_helper = "Key for {}"
    result_helper = "Result of {}"
    if DecOrEn == 'encrypt':
        if OutOrIn == 'in':
            return help_inside_encrypt
        elif OutOrIn == 'out':
            return help_outside_encrypt
    elif DecOrEn == 'decrypt':
        if OutOrIn == 'in':
            return help_inside_decrypt
        elif OutOrIn == 'out':
            return help_outside_decrypt
    elif DecOrEn == 'options':
        return options
    elif DecOrEn == 'helper':
        if OutOrIn == 'msg':
            return msg_helper
        elif OutOrIn == 'key':
            return key_helper
        elif OutOrIn == 'result':
            return result_helper
    elif DecOrEn == 'author':
        return about_me
    
    
    
    
    
        