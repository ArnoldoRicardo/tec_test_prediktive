import json

def get_data(model_id: int, year: int) -> dict:

    file = open('./api-response.json')
    data = json.load(file)
    
    model = data.get(str(model_id), None)

    if not model:
        return "ID doesn't exist"

    piriod = model['schedule']['years'].get(str(year), None)

    if not piriod:
        return "date doesn't exist"

    market_ratio = piriod['marketRatio']
    auction_ratio = piriod['auctionRatio']
    cost = model['saleDetails']['cost']

    auction = market_ratio * cost
    market = auction_ratio * cost

    return {
        'auction': auction,
        'market': market
    }


def main() -> None:
    test1 = get_data(model_id=67352, year=2006)
    print(test1)
    test2 = get_data(model_id=87964, year=2011)
    print(test2)


if __name__ == "__main__":
    main()
