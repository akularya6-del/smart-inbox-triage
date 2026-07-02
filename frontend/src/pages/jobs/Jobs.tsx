import { useState, useEffect } from 'react';
import { api } from '../../lib/api';
import { Activity, Clock, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { toast } from 'sonner';

export default function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const fetchJobs = async () => {
    try {
      setIsLoading(true);
      const { data } = await api.get(`/jobs/`);
      setJobs(data);
    } catch (err) {
      toast.error('Failed to fetch jobs');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  return (
    <div className="flex flex-col h-full space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold tracking-tight">Jobs & Logs</h2>
        <button 
          onClick={fetchJobs}
          className="flex items-center gap-2 bg-secondary text-secondary-foreground px-4 py-2 rounded-md font-medium text-sm hover:bg-secondary/80 transition-colors"
        >
          <Activity className="w-4 h-4" />
          Refresh
        </button>
      </div>

      <div className="flex-1 overflow-auto bg-card rounded-lg border border-border shadow-sm">
        {isLoading ? (
          <div className="flex h-full items-center justify-center text-muted-foreground">Loading...</div>
        ) : jobs.length === 0 ? (
          <div className="flex h-full flex-col items-center justify-center text-muted-foreground gap-2">
            <Clock className="w-8 h-8 opacity-50" />
            <p>No jobs recorded yet.</p>
          </div>
        ) : (
          <div className="divide-y divide-border">
            {jobs.map((job: any) => (
              <div key={job.id} className="p-4 flex flex-col md:flex-row md:items-center justify-between gap-4 hover:bg-secondary/20 transition-colors">
                <div>
                  <h4 className="font-semibold text-sm flex items-center gap-2">
                    {job.name}
                    <span className={`text-[10px] px-1.5 py-0.5 rounded uppercase font-bold ${
                      job.status === 'COMPLETED' ? 'bg-success/20 text-success' :
                      job.status === 'FAILED' ? 'bg-destructive/20 text-destructive' :
                      'bg-warning/20 text-warning'
                    }`}>
                      {job.status}
                    </span>
                  </h4>
                  <p className="text-xs text-muted-foreground mt-1">
                    Job ID: {job.id}
                  </p>
                </div>
                {job.logs && job.logs.length > 0 && (
                  <div className="text-xs flex items-center gap-4 bg-background px-3 py-1.5 rounded-md border border-border">
                    <span className="flex items-center gap-1 text-muted-foreground">
                      <CheckCircle2 className="w-3.5 h-3.5 text-success" />
                      {job.logs[0].items_processed} processed
                    </span>
                    <span className="flex items-center gap-1 text-muted-foreground">
                      <AlertTriangle className="w-3.5 h-3.5 text-destructive" />
                      {job.logs[0].errors} errors
                    </span>
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
