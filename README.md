# TaxMitra - AI Tax Assistant

TaxMitra is an intelligent tax assistant that helps users with:
- Providing accurate tax information based on country-specific regulations
- Calculating tax liabilities using latest rates and rules
- Answering tax-related queries
- Offering personalized tax advice

## Features
- Real-time web search for latest tax information and rates
- Dynamic tax calculations using latest official data
- Cross-referencing multiple authoritative sources
- Fact-checking across government websites
- Secure and private

## Tech Stack
- FastAPI (Backend Framework)
- Phidata (Web Search and Knowledge)
- Python (Core Logic)
- Mathematical Libraries (NumPy, Pandas)

## Getting Started

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn phidata numpy pandas
   ```
4. Set up environment variables:
   - Create a `.env` file
   - Add your Phidata API key
5. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure
- `/app` - Main application code
  - `/api` - API endpoints
  - `/core` - Core tax calculation logic
  - `/utils` - Utility functions
- `/tests` - Test cases
- `main.py` - Application entry point

## How It Works
1. User submits a tax query or calculation request
2. System searches for:
   - Latest tax brackets and rates
   - Current deduction rules
   - Official calculation formulas
3. Information is verified across multiple sources
4. Calculations are performed using the latest verified data
5. Results are presented with source citations

## Tax Calculation Process
1. Fetch current tax brackets and rates from official sources
2. Apply standard mathematical formulas
3. Verify calculations against official examples
4. Present results with sources and explanations

## Tax Calculation Features
- Income tax calculations
- Tax bracket analysis
- Deduction calculations
- Tax optimization suggestions
- Multi-country tax rules

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License
MIT