from prettytable import PrettyTable
from colortable import table
from docs import helper
import platform 
import random
__platform__ = platform.platform()

def Table_maker(msg,key,result,DecOrEn):
  encOrdec = ['encrypt','encryption','decrypt','decryption']
  if DecOrEn == 'encrypt':
      encOrdec.pop(2)
      encOrdec.pop()
  elif DecOrEn == 'decrypt':
      encOrdec.pop(0)
      encOrdec.pop(0)

  help_msg = helper.help_('helper','msg').format(encOrdec[0])
  help_key = helper.help_('helper','key').format(encOrdec[1])
  help_result = helper.help_('helper','result').format(encOrdec[1])
  if __platform__.startswith('Linux'):
    header = ['Types','Information','Helper']
    rows = [["Message", msg, help_msg],["Key", key,help_key],["Result",result,help_result]]
    table_maker = table(rows,header,colorfmt='green')
    return table_maker
  else:
    table_maker = PrettyTable()
    table_maker.title = "Information Box"
    table_maker.field_names = ["Types", "Information","Helper"]
    table_maker.add_row(["Message", msg, help_msg])
    table_maker.add_row(["Key", key, help_key])
    table_maker.add_row(["Result",result,help_result])
    table_maker.align = "l"
    table_maker.align["Information"] = 'c'
    table_maker.align["Types"] = 'c'
    table_maker.max_width = 120
    table_maker.hrules = 1
    return table_maker
    
def Table_maker_multi(msg,keys,result,DecOrEn,types): 
    keys_ID = ["Key A","Key B","Key C","Key D","Key E","Key F","Key G","Key H","Key I"]
    encOrdec = ['encrypt','encryption','decrypt','decryption']
    if DecOrEn == 'encrypt':
      encOrdec.pop(2)
      encOrdec.pop()
    elif DecOrEn == 'decrypt':
      encOrdec.pop(0)
      encOrdec.pop(0)
    help_msg = helper.help_('helper','msg').format(encOrdec[0])
    help_key = helper.help_('helper','key').format(encOrdec[1])
    help_result = helper.help_('helper','result').format(encOrdec[1])
    if __platform__.startswith('Linux'):
        if types == 'affine':
            for i in range(7):
                keys_ID.pop()
            header = ['Types','Information','Helper']
            rows = [["Message", msg, help_msg]]
            for i in range(0,len(keys_ID)):
                rows += [[keys_ID[i],keys[i],help_key]]
            rows += [["Result",result,help_result]]
            table_maker = table(rows,header,colorfmt='green')
            return table_maker


































    
    
    
    
#EOF