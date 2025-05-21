import * as Query from '../adzuna/query'
import * as Parse from '../adzuna/parse'
import * as Auth from '../supabase/auth'

export default function App() {

  return (
    <div className="df flex-col vh-100">
      <header>
        <h1 className="mt0 mb0">Create New App</h1>
        <div>By Pouya Khoshnavazi</div>
      </header>

      <section>
        <div>
          Your application starts in the{' '}
          <code>
            src/<span className="b white">entry.jsx</span>
          </code>{' '}
          file.
        </div>

        <div>
          The component you're looking here at can be found in{' '}
          <code>
            src/components/<span className="b white">App.jsx</span>
          </code>
        </div>

        <div>
          Now go! Save the world with <span className="gold">JavaScript</span>!
        </div>

      </section>
    </div>
  )
}
