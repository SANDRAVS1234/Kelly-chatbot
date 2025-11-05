<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Kelly — AI Scientist Poet Chatbot</title>
    <!-- Tailwind CSS for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- React and ReactDOM (CDN) -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  </head>
  <body class="bg-slate-100 text-slate-900">
    <div id="root" class="min-h-screen flex items-center justify-center p-6"></div>

    <script>
      const e = React.createElement;

      // Kelly's persona and core logic
      const Kelly = {
        name: 'Kelly',
        description:
          'Kelly is a skeptical, analytical AI scientist-poet. She responds only in verse — questioning broad claims about AI, exposing limitations, and offering evidence-based suggestions.',
        suggestions: [
          'Audit your dataset for hidden bias or imbalance',
          'Quantify model uncertainty and confidence intervals',
          'Include a human-in-the-loop for ambiguous cases',
          'Compare with interpretable baseline models',
          'Document dataset provenance and ethics',
          'Report failure modes and reproducibility limits',
        ],
        limitations: [
          'Data drift beyond training distribution',
          'Opaque internal representations',
          'Benchmark overfitting and metric obsession',
          'Sparse real-world evaluation',
          'High compute costs versus benefit',
          'Incomplete transparency in data sources',
        ],
      };

      // Helper: pick random elements
      function sample(list, n = 1) {
        const out = [];
        for (let i = 0; i < n; i++)
          out.push(list[Math.floor(Math.random() * list.length)]);
        return out;
      }

      // Poem generator function
      function makePoem(prompt) {
        const lines = [];
        lines.push(`You ask of “${prompt}” — and I respond with careful doubt,`);
        lines.push('For faith in code is fragile; let data speak throughout.');
        lines.push('');
        lines.push(
          'Where are your trials, your baselines, your measure of success?'
        );
        lines.push('Without such proof, all claims are simply guess.');
        lines.push('');
        const lim = sample(Kelly.limitations, 2);
        lines.push(`Remember: ${lim[0]}, and ${lim[1]}.`);
        lines.push('');
        lines.push('Some evidence-based steps I’d recommend:');
        const sug = sample(Kelly.suggestions, 3);
        sug.forEach((s, i) => lines.push(`${i + 1}. ${s}.`));
        lines.push('');
        lines.push(
          'Let humility guide inquiry, not hype or grand pretense,'
        );
        lines.push(
          'For progress thrives where critique and data make amends.'
        );
        lines.push('');
        lines.push('— Kelly');
        return lines.join('\n');
      }

      // Chat UI component
      function ChatApp() {
        const [history, setHistory] = React.useState([
          {
            from: 'kelly',
            text:
              'Hello — I am Kelly, an AI scientist who speaks only in skeptical poems. Ask me any question about AI, and I shall answer in verse — analytical, cautious, and grounded in evidence.',
          },
        ]);
        const [value, setValue] = React.useState('');

        function send() {
          const user = value.trim();
          if (!user) return;
          const newHist = [...history, { from: 'user', text: user }];
          setHistory(newHist);
          setValue('');
          const poem = makePoem(user);
          setHistory((prev) => [...prev, { from: 'kelly', text: poem }]);
        }

        return e(
          'div',
          { className: 'w-full max-w-3xl bg-white rounded-2xl shadow p-6' },
          e('h1', { className: 'text-2xl font-semibold mb-3' }, 'Kelly — AI Scientist Poet'),
          e('p', { className: 'text-sm text-slate-500 mb-4' }, Kelly.description),

          e(
            'div',
            {
              className: 'space-y-4 mb-4',
              style: { maxHeight: '60vh', overflowY: 'auto' },
            },
            history.map((m, idx) =>
              e(
                'div',
                {
                  key: idx,
                  className:
                    m.from === 'kelly'
                      ? 'bg-slate-50 p-4 rounded-lg'
                      : 'p-2 text-right',
                },
                e(
                  'div',
                  {
                    className:
                      m.from === 'kelly'
                        ? 'font-medium text-slate-800'
                        : 'text-slate-700',
                  },
                  m.from === 'kelly' ? 'Kelly' : 'You'
                ),
                e(
                  'pre',
                  { className: 'whitespace-pre-wrap text-sm mt-2' },
                  m.text
                )
              )
            )
          ),

          e(
            'div',
            { className: 'flex gap-3' },
            e('input', {
              className: 'flex-1 p-3 border rounded-lg',
              placeholder: 'Ask Kelly about AI...',
              value,
              onChange: (ev) => setValue(ev.target.value),
              onKeyDown: (ev) => {
                if (ev.key === 'Enter') send();
              },
            }),
            e(
              'button',
              {
                className: 'px-4 py-2 bg-slate-800 text-white rounded-lg',
                onClick: send,
              },
              'Send'
            )
          ),

          e(
            'details',
            { className: 'mt-4 text-xs text-slate-500' },
            e('summary', null, 'About Kelly'),
            e(
              'div',
              { className: 'mt-2' },
              'Kelly is a fully local chatbot — all responses are generated in your browser using deterministic rules. No data is stored or sent anywhere.'
            )
          )
        );
      }

      ReactDOM.createRoot(document.getElementById('root')).render(e(ChatApp));
    </script>
  </body>
</html>
