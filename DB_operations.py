class DB:
    def __init__(self):
        import sqlite3
        self.connection = sqlite3.connect("MyCircket.db")
        self.cur = self.connection.cursor()
        
    def insert_player(self,team,player,ctg):
        sql='''insert into teams(name,players,value)
                values('{}','{}','{}')'''.format(team,player,ctg)
        self.cur.execute(sql)
    
    def max_wktkpr_value(self):
        sql = '''select MAX(value) from stats where ctg = "WK"'''
        value = self.cur.execute(sql)
        return value.fetchone()[0]
    
    def get_teams(self,key=''):
        sql='''select * from teams'''
        records=self.cur.execute(sql)
        if key != '':
            results = [record[1] for record in records if key in record]
        else:            
            results = set([record[0] for record in records])
        return results
        
    def get_match_details(self,team_name):
        sql = '''select * from match
                inner join teams on match.player = teams.players 
                where teams.name = "{}"'''.format(team_name)
        records = self.cur.execute(sql)
        results = [record for record in records]
        return results
    
    def get_stats(self,key,feild):
        sql = '''select * from stats'''
        records  = self.cur.execute(sql)
        results = [record for record in records]
        
        if feild == "value":
            result = [result[-2] for result in results if key in result][0]
        elif feild == "ctg":
            result = [result[-1] for result in results if key in result][0]
        else:
            result = [result[0] for result in results if key in result]
            
        return result
    
    def close(self):
        self.connection.commit()
        self.connection.close()
    


#print(get_teams())
#connection.close()
#cur.execute("insert into teams(name,players,value) values('Aj','p1',123)")
