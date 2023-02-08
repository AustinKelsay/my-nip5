# my-nip5

This is a single purpose Flask application that serves a nostr.json endpoint for NIP-05 compatibility. The purpose of my-nip5 is to provide a simple free template that allows you to deploy a server for verifying your NOSTR profile with YOUR OWN custom domain.

## Updating the Variables

To update the variables in the nostr_data dictionary, open the app.py file and update the values for your NOSTR alias and public key in hex format:

`nostr_data = {
    "names": {
        "<YOUR NOSTR ALIAS>": "<YOUR NOSTR PUBLIC KEY IN HEX FORMAT>"
    },
    "relays": {
        "<YOUR NOSTR PUBLIC KEY IN HEX FORMAT>": ["wss://relay.example.com", "wss://relay2.example.com"]
    }
}`

## Deploying to Vercel

To deploy this application to Vercel, follow these steps:

- Clone this repository to your local machine:
`git clone https://github.com/<YOUR REPOSITORY>.git`
- Navigate to the project directory:
`cd nostr-json-endpoint`
- Log in to your Vercel account:
`vercel login`
- Initialize the project with Vercel:
`vercel init`
- Deploy the application to Vercel:
`vercel`

After the deployment is complete, you will receive a URL for your application, for example https://nostr-json-endpoint.vercel.app.

## Adding a Custom Domain

To add a custom domain on Vercel, follow these steps:

- Go to your project on Vercel and click on the "Domains" tab.
- Click on the "Add Domain" button.
- Enter your custom domain, for example nostr.example.com.
- Follow the instructions for configuring your domain's DNS records, provided by Vercel.
- Wait for the domain to propagate and refresh the page.
- Your custom domain should now be configured and accessible.

## Testing the Endpoint

You can test the nostr.json endpoint by visiting https://<YOUR DOMAIN>/.well-known/nostr.json?name=<YOUR NOSTR ALIAS> in your web browser or using a tool such as curl:

`curl https://<YOUR DOMAIN>/.well-known/nostr.json?name=<YOUR NOSTR ALIAS>`

You should receive a JSON response containing your NOSTR data.
