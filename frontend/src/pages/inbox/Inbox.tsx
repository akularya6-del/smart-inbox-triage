import { useState, useEffect } from 'react';
import { api } from '../../lib/api';
import { RefreshCw, Search, Filter } from 'lucide-react';
import { toast } from 'sonner';

export default function Inbox() {
  const [emails, setEmails] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isSyncing, setIsSyncing] = useState(false);

  // In a real app we'd get this from a React Context or Auth Provider
  // Hardcoding for MVP flow assumption
  const userId = localStorage.getItem("user_id") || "test_user_id";

  const fetchEmails = async () => {
    try {
      setIsLoading(true);
      const { data } = await api.get(`/emails/?user_id=${userId}`);
      setEmails(data);
    } catch (err) {
      toast.error('Failed to fetch emails');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSync = async () => {
    try {
      setIsSyncing(true);
      const { data } = await api.post(`/emails/sync?user_id=${userId}`);
      toast.success(`Sync complete. Processed ${data.processed} emails.`);
      fetchEmails();
    } catch (err) {
      toast.error('Failed to sync emails');
    } finally {
      setIsSyncing(false);
    }
  };

  useEffect(() => {
    fetchEmails();
  }, []);

  return (
    <div className="flex flex-col h-full space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold tracking-tight">Inbox</h2>
        <div className="flex gap-2">
          <button 
            onClick={handleSync}
            disabled={isSyncing}
            className="flex items-center gap-2 bg-primary text-primary-foreground px-4 py-2 rounded-md font-medium text-sm hover:bg-primary/90 transition-colors disabled:opacity-50"
          >
            <RefreshCw className={`w-4 h-4 ${isSyncing ? 'animate-spin' : ''}`} />
            {isSyncing ? 'Syncing...' : 'Manual Sync'}
          </button>
        </div>
      </div>
      
      <div className="flex gap-2 border-b border-border pb-4">
        <div className="relative flex-1">
          <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
          <input 
            type="text" 
            placeholder="Search emails..." 
            className="w-full pl-9 pr-4 py-2 bg-secondary border-none rounded-md text-sm outline-none focus:ring-1 focus:ring-primary"
          />
        </div>
        <button className="flex items-center justify-center bg-secondary px-3 py-2 rounded-md">
          <Filter className="w-4 h-4 text-muted-foreground" />
        </button>
      </div>

      <div className="flex-1 overflow-auto bg-card rounded-lg border border-border shadow-sm">
        {isLoading ? (
          <div className="flex h-full items-center justify-center text-muted-foreground">Loading...</div>
        ) : emails.length === 0 ? (
          <div className="flex h-full items-center justify-center text-muted-foreground flex-col gap-2">
            <p>No emails found.</p>
            <p className="text-sm">Click "Manual Sync" to fetch unread emails from Gmail.</p>
          </div>
        ) : (
          <div className="divide-y divide-border">
            {emails.map((email: any) => (
              <div key={email.id} className="p-4 hover:bg-secondary/20 transition-colors cursor-pointer group flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-primary/20 flex items-center justify-center text-primary font-bold uppercase shrink-0">
                  {email.sender_name.charAt(0)}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex justify-between items-start mb-1">
                    <span className="font-semibold text-sm truncate">{email.sender_name}</span>
                    <span className="text-xs text-muted-foreground whitespace-nowrap ml-2">Just now</span>
                  </div>
                  <h4 className="text-sm font-medium truncate mb-1">{email.subject}</h4>
                  <p className="text-xs text-muted-foreground line-clamp-2">{email.snippet}</p>
                </div>
                {email.classification && (
                  <div className="shrink-0 bg-accent/20 text-accent font-medium px-2 py-1 rounded text-[10px] uppercase border border-accent/30">
                    {email.classification}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
