jedis = {
    "luke": "Jedi",
    "yoda": "Jedi Master",
    "anakin": "Sith Lord",
    "obi_wan": "Jedi Knight",
    "han_solo": "Smuggler",
}

jedis.update({"chewbacca": "Wookiee"})
jedis["luke"] = "Jedi Knight"
print(jedis)


print(jedis.get("luke"))

siths = {
         "Palpatine" : {"lighsaber": "red", "age": 55, "apprentice": "Darth Maul"},
         "Dooku": ["Count Dooku", "Darth Tyranus"],
}


print(siths["Palpatine"]["apprentice"])

warehouse_stocks = {"banana": 5, "apple": 10, "orange": 8}
print(warehouse_stocks["banana"])

print(jedis.items())
print(jedis.values())


drilling_machine = {
    "machine_id": "DM-001",
    "name": "Deep Driller 3000",
    "location": {
        "latitude": 29.7355,
        "longitude": -95.3635,
        "region": "Gulf of Mexico",
        "country": "USA",
    },
}
print(drilling_machine["location"]["country"])
