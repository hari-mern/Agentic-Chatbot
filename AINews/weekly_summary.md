# Weekly AI News


<think>
Here's a thinking process:

1.  **Analyze User Input:**
   - **Task:** Summarize AI news articles into markdown format.
   - **Requirements per item:**
     - Date in **YYYY-MM-DD** format in IST timezone
     - Concise sentence summary from the latest news
     - Sort news by date (latest first)
     - Source URL as link
   - **Format:**
     ### [Date]
     - [Summary](URL)
   - **Input Data:** 5 articles with content, URL, and Date (in GMT or other formats).

2.  **Process Each Article:**
   I need to extract the date, convert it to IST (UTC+5:30), format it as YYYY-MM-DD, write a concise summary, and note the URL. Then sort by date descending.

   *Article 1:*
   - Content: Indian manufacturers betting heavily on AI, but lag China on innovation (PwC study). 16% anchor strategy in product leadership vs 63% in China. Automation rising across value chain. 59% expect AI to be crucial for strategic goals vs 52% globally.
   - URL: https://www.consultancy.in/news/amp/4537/indian-manufacturers-race-ahead-on-ai-but-lag-china-on-innovation
   - Date: Mon, 17 Aug 2026 06:30:00 GMT
   - Convert to IST: GMT + 5:30 = 12:00 IST on 17 Aug 2026. Date: 2026-08-17
   - Summary: Indian manufacturers are increasing AI adoption across operations but significantly lag behind Chinese peers in innovation-driven product leadership, according to a PwC study.

   *Article 2:*
   - Content: ET Prime special series... mentions "AI is powering US GDP: Why India cannot afford to be left behind" and URL suggests "global-ai-investment-1-trillion-in-2026-to-reach-1-4-global-gdp-by-2028-goldman-sachs". The content seems to be a webpage listing multiple articles, but the URL clearly points to Goldman Sachs forecasting $1 trillion global AI investment in 2026, reaching 1.4% of global GDP by 2028.
   - URL: http://economictimes.indiatimes.com/tech/artificial-intelligence/global-ai-investment-1-trillion-in-2026-to-reach-1-4-global-gdp-by-2028-goldman-sachs/articleshow/133285754.cms
   - Date: Mon, 17 Aug 2026 06:00:00 GMT
   - Convert to IST: GMT + 5:30 = 11:30 IST on 17 Aug 2026. Date: 2026-08-17
   - Summary: Goldman Sachs forecasts global AI investment will hit $1 trillion in 2026, potentially contributing 1.4% to global GDP by 2028 as the technology drives economic growth.

   *Article 3:*
   - Content: OpenAI Launches GPT-5 With Native Voice, Visi... (cut off, but implies vision/multimodal). Title: OpenAI Launches GPT-5 With Native Voice, Visi...
   - URL: https://mshale.com/1e85c581/46973104HkUYLB09SA4HVTg
   - Date: Fri, 14 Aug 2026 06:00:00 GMT
   - Convert to IST: GMT + 5:30 = 11:30 IST on 14 Aug 2026. Date: 2026-08-14
   - Summary: OpenAI has launched GPT-5, introducing native voice capabilities and advanced vision features to enhance multimodal AI interactions.

   *Article 4:*
   - Content: Financial Times subscription page text, but the title is "# The AI threat to India’s IT jobs machine".
   - URL: https://www.ft.com/content/dee4bd2c-fbad-4713-9b14-22d441967ce4?syn-25a6b1a6=1
   - Date: Wed, 12 Aug 2026 02:44:49 GMT
   - Convert to IST: GMT + 5:30 = 08:14 IST on 12 Aug 2026. Date: 2026-08-12
   - Summary: Artificial intelligence poses a significant disruption to India's IT services sector, threatening traditional job structures and business models as automation capabilities advance.

   *Article 5:*
   - Content: Nvidia developing Nemotron 4 AI model family to challenge top open-source models. Also unveiled Nemotron 3.5 Lightning and NeMo Switchyard routing library. Formed coalition for AI safety/cybersecurity.
   - URL: https://indianexpress.com/article/technology/artificial-intelligence/nvidia-building-1-trillion-parameter-nemotron-4-to-rival-open-ai-models-report-10829438
   - Date: Wed, 12 Aug 2026 06:41:17 GMT
   - Convert to IST: GMT + 5:30 = 12:11 IST on 12 Aug 2026. Date: 2026-08-12
   - Summary: Nvidia is developing the Nemotron 4 model family to compete with leading open-source AI systems, alongside releasing new tools for code review, security, and automated model routing.

3.  **Sort by Date (Latest First):**
   - 2026-08-17 (Article 1)
   - 2026-08-17 (Article 2)
   - 2026-08-14 (Article 3)
   - 2026-08-12 (Article 4)
   - 2026-08-12 (Article 5)
   Note: For same dates, order doesn't strictly matter, but I'll keep them as is or sort by time if needed. The prompt says "Sort news by date wise (latest first)". I'll list them in descending order.

   Let's verify IST conversion:
   - 17 Aug 2026 06:30 GMT -> +5:30 = 12:00 IST -> 2026-08-17
   - 17 Aug 2026 06:00 GMT -> +5:30 = 11:30 IST -> 2026-08-17
   - 14 Aug 2026 06:00 GMT -> +5:30 = 11:30 IST -> 2026-08-14
   - 12 Aug 2026 02:44 GMT -> +5:30 = 08:14 IST -> 2026-08-12
   - 12 Aug 2026 06:41 GMT -> +5:30 = 12:11 IST -> 2026-08-12
   All dates remain the same in YYYY-MM-DD format since the time shift doesn't cross midnight.

4.  **Format Output:**
   Check format requirement:
   ### [Date]
   - [Summary](URL)

   I will structure it exactly as requested.

   Draft:
   ### 2026-08-17
   - Indian manufacturers are rapidly scaling AI adoption across operations but significantly lag Chinese peers in innovation-driven product leadership, according to a PwC study.[](https://www.consultancy.in/news/amp/4537/indian-manufacturers-race-ahead-on-ai-but-lag-china-on-innovation)
   - Goldman Sachs forecasts global AI investment will reach $1 trillion in 2026, potentially contributing 1.4% to global GDP by 2028 as the technology accelerates economic growth.[](http://economictimes.indiatimes.com/tech/artificial-intelligence/global-ai-investment-1-trillion-in-2026-to-reach-1-4-global-gdp-by-2028-goldman-sachs/articleshow/133285754.cms)

   ### 2026-08-14
   - OpenAI has launched GPT-5, introducing native voice capabilities and advanced vision features to enhance multimodal AI interactions.[](https://mshale.com/1e85c581/46973104HkUYLB09SA4HVTg)

   ### 2026-08-12
