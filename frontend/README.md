# Emerald Frontend

A modern SvelteKit frontend for the Emerald esoteric education platform, teaching Tarot, Qabalah, and Astrology through structured curriculum.

## Tech Stack

- **Framework**: SvelteKit (Svelte 5)
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **HTTP Client**: Native Fetch API
- **Build Tool**: Vite

## Prerequisites

- Node.js 18+
- npm or pnpm
- Backend API running on `http://localhost:5000`

## Getting Started

### 1. Install Dependencies

```bash
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:5173` (or another port if 5173 is in use).

To open the app automatically in your browser:

```bash
npm run dev -- --open
```

### 3. Start the Backend API

Make sure the Flask backend API is running on port 5000:

```bash
cd ..
python app.py
```

The frontend expects the API to be available at `http://localhost:5000`.

## Project Structure

```
frontend/
├── src/
│   ├── routes/
│   │   ├── +layout.svelte    # Root layout with header/footer
│   │   └── +page.svelte       # Home page with card grid
│   ├── lib/
│   │   ├── api.ts             # API client functions
│   │   ├── types.ts           # TypeScript interfaces
│   │   └── assets/            # Static assets
│   ├── components/            # Reusable components (to be added)
│   ├── app.css                # Global styles + Tailwind config
│   └── app.html               # HTML template
├── static/                    # Static files
└── package.json
```

## Design System

### Color Palette

- **Emerald** (`#50C878`): Primary brand color, links, CTAs
- **Gold** (`#D4AF37`): Highlights, important information
- **Black** (`#0F0F0F`): Primary text color
- **Cream** (`#F4ECD8`): Background color
- **Charcoal** (`#2B2B2B`): Secondary backgrounds, headers

### Using Colors in Tailwind

The custom colors are available as Tailwind classes:

```html
<div class="bg-emerald text-cream">Emerald background</div>
<h1 class="text-gold">Gold heading</h1>
<button class="bg-charcoal hover:bg-emerald">Button</button>
```

## API Client

The `src/lib/api.ts` module provides functions to interact with the backend:

```typescript
import { getCards, getCard, getCardWithCorrespondences } from '$lib/api';

// Get all cards
const cards = await getCards();

// Get cards with filters
const majorArcana = await getCards({ arcana: 'Major Arcana' });
const wands = await getCards({ suit: 'Wands' });

// Get single card
const fool = await getCard(0);

// Get card with full correspondences
const foolWithCorrespondences = await getCardWithCorrespondences(0);
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run check` - Run TypeScript type checking
- `npm run check:watch` - Run type checking in watch mode

## Building for Production

```bash
npm run build
```

The production build will be in the `build/` directory. Preview it with:

```bash
npm run preview
```

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

## Features

### Current Features

- ✅ View all 78 tarot cards in a responsive grid
- ✅ Card filtering by arcana, suit, and element
- ✅ Clean, modern design with Emerald color palette
- ✅ Responsive layout (mobile, tablet, desktop)
- ✅ Loading and error states
- ✅ TypeScript type safety

### Upcoming Features

- 🔜 Individual card detail pages
- 🔜 Full correspondence display (Qabalah, Astrology)
- 🔜 Search and advanced filtering
- 🔜 Daily card draw feature
- 🔜 Learning modules and curriculum
- 🔜 User authentication and progress tracking

## Development Guidelines

- Use TypeScript for all new code
- Follow the existing component structure
- Maintain responsive design principles
- Keep the design clean and modern (not witchy/mystical)
- Use generous whitespace
- Test on multiple screen sizes

## Troubleshooting

### Backend Connection Issues

If you see "Error Loading Cards", ensure:

1. The backend API is running: `python app.py` in the root directory
2. The API is accessible at `http://localhost:5000`
3. CORS is properly configured in the backend

### Port Already in Use

If port 5173 is already in use, Vite will automatically use the next available port. Check the terminal output for the actual URL.

## Resources

- [SvelteKit Documentation](https://kit.svelte.dev)
- [Svelte 5 Documentation](https://svelte.dev/docs/svelte/overview)
- [Tailwind CSS v4 Documentation](https://tailwindcss.com/docs)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)

## License

Part of the Emerald esoteric education platform.
