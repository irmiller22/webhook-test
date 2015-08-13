# Webhooks on GitHub

## How it works

Any time a push event occurs on a repo that you're tracking (for GitHub), a
webhook will fire to a URL that you specify. In this case, we have the
root URL looking for a `POST` request.

## Unsecure Webhook

What's involved in getting a webhook through to your application? You
just need to pull the data out of the request object that hits the
`POST` action in the specified route inside your application. For
example, if you're listening for a push event on the `/push` URL, then
you should expect a request object when the `POST` request comes in from
the GitHub webhook.

Once you parse the request object properly, you're able to obtain all
the necessary data of that push event.

## Secure Webhook

