def team_lineup(*teams):
   team_dict = {}

   for name, country in teams:
      if country not in team_dict:
         team_dict[country] = [name]
      else:
         team_dict[country].append(name)

   result = sorted(team_dict.items(), key = lambda x: (-len(x[-1]), x[0]))
   message = ""
   for country, players in result:
       message += f'{country}:\n'
       for player in players:
          message += f"  -{player}\n"

   return message


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
