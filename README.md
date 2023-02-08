# my-nip5

This is a simple, ready-to-deploy Flask application designed to serve a nostr.json endpoint for NIP-05 compatibility. The purpose of this template is to make it easy and free for you to host and verify your NOSTR profile with your own custom domain, by deploying it on Vercel. With just a few updates to the provided code, you can have your own NIP-05 verification server up and running in no time.

## Updating the Variables

To update the variables in the nostr_data dictionary, open the app.py file and update the values for your NOSTR alias and public key in hex format:

`nostr_data = {
    "names": {
        "<YOUR NOSTR ALIAS>": "<YOUR NOSTR PUBLIC KEY IN HEX FORMAT>"
    }
}`

## Deploying to Vercel

To deploy this application to Vercel, follow these steps:

- Clone this repository to your local machine:
`git clone https://github.com/AustinKelsay/my-nip5.git`
- Navigate to the project directory:
`cd my-nip5`
- Log in to your Vercel account:
`vercel login`
- Initialize the project with Vercel:
`vercel init`
- Deploy the application to Vercel:
`vercel`

After the deployment is complete, you will receive a URL for your application, for example https://my-nip5.vercel.app.

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
