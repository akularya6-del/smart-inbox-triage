import { Routes, Route } from 'react-router-dom'
import { Inbox, Settings, Activity, ListCheck, GitPullRequest } from 'lucide-react'

// Layout shell component (will extract later)
function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen w-full bg-background overflow-hidden">
      <aside className="w-64 border-r border-border bg-card/50 flex flex-col">
        <div className="h-14 border-b border-border flex items-center px-4">
          <h1 className="font-bold text-lg text-primary flex items-center gap-2">
            <Inbox className="w-5 h-5" /> Smart Triage
          </h1>
        </div>
        <nav className="flex-1 overflow-y-auto p-4 space-y-2">
          <a href="/" className="flex items-center gap-3 px-3 py-2 rounded-md bg-secondary text-secondary-foreground text-sm font-medium transition-colors hover:bg-secondary/80">
            <Inbox className="w-4 h-4" /> Inbox
          </a>
          <a href="/review" className="flex items-center gap-3 px-3 py-2 rounded-md text-muted-foreground hover:bg-secondary/50 hover:text-foreground text-sm font-medium transition-colors">
            <ListCheck className="w-4 h-4" /> Review Queue
          </a>
          <a href="/rules" className="flex items-center gap-3 px-3 py-2 rounded-md text-muted-foreground hover:bg-secondary/50 hover:text-foreground text-sm font-medium transition-colors">
            <GitPullRequest className="w-4 h-4" /> Rules
          </a>
          <a href="/jobs" className="flex items-center gap-3 px-3 py-2 rounded-md text-muted-foreground hover:bg-secondary/50 hover:text-foreground text-sm font-medium transition-colors">
            <Activity className="w-4 h-4" /> Jobs & Logs
          </a>
        </nav>
        <div className="p-4 border-t border-border">
          <a href="/settings" className="flex items-center gap-3 px-3 py-2 rounded-md text-muted-foreground hover:bg-secondary/50 hover:text-foreground text-sm font-medium transition-colors">
            <Settings className="w-4 h-4" /> Settings
          </a>
        </div>
      </aside>
      <main className="flex-1 flex flex-col min-w-0">
        <header className="h-14 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 flex items-center justify-between px-4">
          <div className="flex items-center gap-4">
            <h2 className="text-sm font-semibold">Dashboard</h2>
          </div>
        </header>
        <div className="flex-1 overflow-auto p-6">
          {children}
        </div>
      </main>
    </div>
  )
}

import Login from './pages/auth/Login'
import AuthCallback from './pages/auth/AuthCallback'
import Inbox from './pages/inbox/Inbox'
import Rules from './pages/rules/Rules'
import Review from './pages/review/Review'
import Settings from './pages/settings/Settings'
import Jobs from './pages/jobs/Jobs'

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/api/auth/callback/google" element={<AuthCallback />} />
      <Route path="/*" element={
        <AppLayout>
          <Routes>
            <Route path="/" element={<Inbox />} />
            <Route path="/review" element={<Review />} />
            <Route path="/rules" element={<Rules />} />
            <Route path="/jobs" element={<Jobs />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </AppLayout>
      } />
    </Routes>
  )
}

export default App
