def tournamentWinner(competitions, results):
    currentBestTeam = ""
    mapOfWinners = {currentBestTeam:0}
    for index, result in enumerate(results):
        homeTeam,awayTeam = competitions[index]

        winner = homeTeam if result == 1 else awayTeam
        if mapOfWinners.__contains__(winner):
            mapOfWinners[winner] += 3
        else:
            mapOfWinners[winner] = 3
        if mapOfWinners[winner]>mapOfWinners[currentBestTeam]:
            currentBestTeam = winner

    return currentBestTeam

if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]

    results = [0, 0, 1]

    tournamentWinner(competitions, results)
