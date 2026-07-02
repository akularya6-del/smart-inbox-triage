import { useState, useEffect } from 'react';
import { api } from '../../lib/api';
import { GitPullRequest, Plus, Trash2 } from 'lucide-react';
import { toast } from 'sonner';

export default function Rules() {
  const [rules, setRules] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  
  const userId = localStorage.getItem("user_id") || "test_user_id";

  const fetchRules = async () => {
    try {
      setIsLoading(true);
      const { data } = await api.get(`/rules/?user_id=${userId}`);
      setRules(data);
    } catch (err) {
      toast.error('Failed to fetch rules');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (id: string) => {
    try {
      await api.delete(`/rules/${id}`);
      toast.success('Rule deleted');
      fetchRules();
    } catch (err) {
      toast.error('Failed to delete rule');
    }
  };

  useEffect(() => {
    fetchRules();
  }, []);

  return (
    <div className="flex flex-col h-full space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold tracking-tight">Rules Engine</h2>
        <button className="flex items-center gap-2 bg-primary text-primary-foreground px-4 py-2 rounded-md font-medium text-sm hover:bg-primary/90 transition-colors">
          <Plus className="w-4 h-4" />
          Create Rule
        </button>
      </div>

      <div className="flex-1 overflow-auto bg-card rounded-lg border border-border shadow-sm">
        {isLoading ? (
          <div className="flex h-full items-center justify-center text-muted-foreground">Loading...</div>
        ) : rules.length === 0 ? (
          <div className="flex h-full flex-col items-center justify-center text-muted-foreground gap-2">
            <GitPullRequest className="w-8 h-8 opacity-50" />
            <p>No rules defined yet.</p>
          </div>
        ) : (
          <div className="divide-y divide-border">
            {rules.map((rule: any) => (
              <div key={rule.id} className="p-4 flex items-center justify-between hover:bg-secondary/20 transition-colors group">
                <div>
                  <h4 className="font-semibold text-sm flex items-center gap-2">
                    {rule.name}
                    {!rule.enabled && <span className="bg-destructive/20 text-destructive text-[10px] px-1.5 py-0.5 rounded uppercase">Disabled</span>}
                  </h4>
                  <p className="text-xs text-muted-foreground mt-1">
                    Action: <span className="font-medium text-foreground">{rule.action}</span> (Priority: {rule.priority})
                  </p>
                </div>
                <button 
                  onClick={() => handleDelete(rule.id)}
                  className="p-2 text-muted-foreground hover:text-destructive hover:bg-destructive/10 rounded-md opacity-0 group-hover:opacity-100 transition-all"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
