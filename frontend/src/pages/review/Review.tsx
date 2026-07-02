import { useState, useEffect } from 'react';
import { api } from '../../lib/api';
import { ListCheck, CheckCircle2, XCircle } from 'lucide-react';
import { toast } from 'sonner';

export default function Review() {
  const [items, setItems] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  
  const userId = localStorage.getItem("user_id") || "test_user_id";

  const fetchQueue = async () => {
    try {
      setIsLoading(true);
      const { data } = await api.get(`/review/?user_id=${userId}`);
      setItems(data);
    } catch (err) {
      toast.error('Failed to fetch review queue');
    } finally {
      setIsLoading(false);
    }
  };

  const handleAction = async (id: string, action: 'approve' | 'reject') => {
    try {
      await api.post(`/review/${id}/${action}`);
      toast.success(`Item ${action}d`);
      fetchQueue();
    } catch (err) {
      toast.error(`Failed to ${action} item`);
    }
  };

  useEffect(() => {
    fetchQueue();
  }, []);

  return (
    <div className="flex flex-col h-full space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold tracking-tight">Review Queue</h2>
      </div>

      <div className="flex-1 overflow-auto bg-card rounded-lg border border-border shadow-sm">
        {isLoading ? (
          <div className="flex h-full items-center justify-center text-muted-foreground">Loading...</div>
        ) : items.length === 0 ? (
          <div className="flex h-full flex-col items-center justify-center text-muted-foreground gap-2">
            <ListCheck className="w-8 h-8 opacity-50" />
            <p>Queue is empty! All clear.</p>
          </div>
        ) : (
          <div className="divide-y divide-border">
            {items.map((item: any) => (
              <div key={item.id} className="p-4 flex flex-col md:flex-row md:items-center justify-between gap-4 hover:bg-secondary/20 transition-colors">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-semibold text-sm">{item.email_sender}</span>
                    <span className="text-xs text-muted-foreground border border-border px-1.5 py-0.5 rounded">
                      {item.reason}
                    </span>
                  </div>
                  <h4 className="text-sm truncate mb-2">{item.email_subject}</h4>
                  <div className="text-xs flex items-center gap-2">
                    <span className="text-muted-foreground">Suggested Action:</span>
                    <span className="bg-primary/20 text-primary font-medium px-2 py-0.5 rounded uppercase">{item.suggested_action}</span>
                    <span className="text-muted-foreground">({item.confidence}% confidence)</span>
                  </div>
                </div>
                <div className="flex items-center gap-2 shrink-0">
                  <button 
                    onClick={() => handleAction(item.id, 'reject')}
                    className="flex items-center gap-2 px-3 py-1.5 border border-border hover:bg-destructive/10 hover:text-destructive hover:border-destructive/30 rounded-md text-sm font-medium transition-colors"
                  >
                    <XCircle className="w-4 h-4" /> Reject
                  </button>
                  <button 
                    onClick={() => handleAction(item.id, 'approve')}
                    className="flex items-center gap-2 px-3 py-1.5 bg-success/20 text-success border border-success/30 hover:bg-success hover:text-success-foreground rounded-md text-sm font-medium transition-colors"
                  >
                    <CheckCircle2 className="w-4 h-4" /> Approve
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
