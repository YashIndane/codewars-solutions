package kata

func GetPlanetName(ID int) string {
    return []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"}[ID-1]
    
}
