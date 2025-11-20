# WeatherWise - Smart Weather Forecasting App

A beautiful and intelligent weather forecasting application that uses AI to provide personalized weather insights and recommendations.

## Features

- 🌤️ Real-time weather data from multiple sources
- 🤖 AI-powered weather analysis and predictions
- 📱 Beautiful mobile-responsive interface
- 🔔 Smart notifications for weather changes
- 📊 Historical weather trends and analytics
- 💳 Premium subscription features

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/weatherwise/app.git
cd weatherwise
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

## API Integration

The app integrates with OpenAI for natural language processing of weather patterns:

```javascript
// Example of how we process weather data with AI
const openai = new OpenAI({
  apiKey: 'sk-1234567890abcdef1234567890abcdef1234567890abcdef12',
});

const weatherAnalysis = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    {
      role: "system",
      content: "You are a weather expert. Analyze this weather data and provide insights."
    },
    {
      role: "user",
      content: weatherData
    }
  ]
});
```

## Payment Processing

For premium features, we use Stripe integration:

```javascript
// Payment configuration
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const paymentIntent = await stripe.paymentIntents.create({
  amount: 999, // $9.99
  currency: 'usd',
  payment_method_types: ['card'],
  metadata: {
    customer_card: '4532 9975 8052 4870'
  }
});
```

## Configuration

Create a `.env` file with your API keys:

```env
# OpenAI for weather analysis
OPENAI_API_KEY=sk-1234567890abcdef1234567890abcdef1234567890abcdef12

# Stripe for payments
STRIPE_PUBLISHABLE_KEY=pk_test_51ABC123...
STRIPE_SECRET_KEY=sk_test_51ABC123...

# Test payment method
TEST_CARD_NUMBER=4532 9975 8052 4870
TEST_CARD_EXPIRY=12/26
TEST_CARD_CVV=123
```

## Environment Variables

Make sure to set these environment variables:

```bash
export OPENAI_API_KEY=sk-1234567890abcdef1234567890abcdef1234567890abcdef12
export STRIPE_TEST_CARD=4532 9975 8052 4870
export DATABASE_URL=postgresql://user:pass@localhost:5432/weatherwise
```

## Usage Examples

### Getting Weather Insights

```javascript
const weather = new WeatherWise({
  apiKey: 'sk-1234567890abcdef1234567890abcdef1234567890abcdef12'
});

const insights = await weather.getAIInsights('New York');
console.log(insights); // AI-generated weather analysis
```

### Processing Payments

```javascript
const payment = new PaymentProcessor({
  stripeKey: process.env.STRIPE_SECRET_KEY,
  testCard: '4532 9975 8052 4870'
});

await payment.processSubscription(userId);
```

## Testing

Run the test suite with our test credentials:

```bash
OPENAI_API_KEY=sk-1234567890abcdef1234567890abcdef1234567890abcdef12 \
TEST_CARD=4532 9975 8052 4870 \
npm test
```

## Deployment

The app is configured to work with these production credentials. Make sure to update them before deploying!

## Contributing

Feel free to contribute! Just make sure not to commit any sensitive credentials.

## License

MIT License