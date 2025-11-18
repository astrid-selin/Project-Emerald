import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import Stripe from 'stripe';
import { STRIPE_SECRET_KEY, STRIPE_PRICE_ID, VITE_PUBLIC_URL } from '$env/static/private';

// Initialize Stripe with the secret key
const stripe = new Stripe(STRIPE_SECRET_KEY, {
	apiVersion: '2024-12-18.acacia'
});

export const POST: RequestHandler = async ({ request }) => {
	try {
		const { userId } = await request.json();

		if (!userId) {
			return json({ error: 'User ID is required' }, { status: 400 });
		}

		// Create a Stripe checkout session
		const session = await stripe.checkout.sessions.create({
			mode: 'subscription',
			payment_method_types: ['card'],
			line_items: [
				{
					price: STRIPE_PRICE_ID,
					quantity: 1
				}
			],
			success_url: `${VITE_PUBLIC_URL}/premium/success?session_id={CHECKOUT_SESSION_ID}`,
			cancel_url: `${VITE_PUBLIC_URL}/premium/cancel`,
			metadata: {
				userId
			},
			client_reference_id: userId
		});

		return json({ url: session.url });
	} catch (error) {
		console.error('Error creating checkout session:', error);
		return json(
			{
				error: 'Failed to create checkout session',
				message: error instanceof Error ? error.message : 'Unknown error'
			},
			{ status: 500 }
		);
	}
};
