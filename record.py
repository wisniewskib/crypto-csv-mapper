class DeltaRecord:
    def __init__(
        self,
        date,
        way,
        baseAmount,
        baseCurrency,
        baseType,
        quoteAmount,
        quoteCurrency,
        exchange,
        sentFrom,
        sentTo,
        feeAmount,
        feeCurrency,
        broker,
        notes,
    ):
        self.date = date
        self.way = way
        self.baseAmount = baseAmount
        self.baseCurrency = baseCurrency
        self.baseType = baseType
        self.quoteAmount = quoteAmount
        self.quoteCurrency = quoteCurrency
        self.exchange = exchange
        self.sentFrom = sentFrom
        self.sentTo = sentTo
        self.feeAmount = feeAmount
        self.feeCurrency = feeCurrency
        self.broker = broker
        self.notes = notes

    def __str__(self):
        return (
            f"Date: {self.date}, Way: {self.way}, Base Amount: {self.baseAmount}, "
            f"Base Currency: {self.baseCurrency}, Base Type: {self.baseType}, "
            f"Quote Amount: {self.quoteAmount}, Quote Currency: {self.quoteCurrency}, "
            f"Exchange: {self.exchange}, Sent From: {self.sentFrom}, Sent To: {self.sentTo}, "
            f"Fee Amount: {self.feeAmount}, Fee Currency: {self.feeCurrency}, "
            f"Broker: {self.broker}, Notes: {self.notes}"
        )
