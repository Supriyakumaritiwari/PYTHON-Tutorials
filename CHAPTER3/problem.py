# WAP to fill ina letter template give below with name and date 

letter = '''
           Dear <|Name|>
           You are selected!
           <|Date|>
            '''
print(letter.replace("<|Name|>","Harry").replace("<|Date|>","04-07-2025"))
