from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp import HttpError



client_id = "AX-Z8VZkypbmvH8OBxovA6u-OzCjwNdBb0k1v-ODc5eFGjVlZ3X0DFLAFPRy_s-0AbGdhbd2rsXgYg-h"
client_secret = "EKDAqqAWNJerQJgVxkkoLX3X6luDF4bor7KtZiOYhkXSXnoBdqexmCHf5Mlj-YZNEpmR_seng_2AzTsZ"


environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(environment)



request = OrdersCreateRequest()

request.prefer('return=representation')

request.request_body (
    {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00"
                }
            }
        ]
    }
)

try:

    response = client.execute(request)
    print('Order With Complete Payload:')
    print('Status Code:', response.status_code)
    print('Status:', response.result.status)
    print('Order ID:', response.result.id)
    print('Intent:', response.result.intent)
    print('Links:')
    for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print('Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code, response.result.purchase_units[0].amount.value))

        order = response.result
        print(order)
except IOError as ioe:
    print(ioe)
    if isinstance(ioe, HttpError):

        print(ioe.status_code)
