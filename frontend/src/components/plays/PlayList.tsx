// src/components/plays/PlayList.tsx
import { useQuery } from 'react-query';
import { getPlays } from '../../services/api';

const PlayList = () => {
  const { data: plays, isLoading, error } = useQuery('plays', getPlays);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading plays</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {plays?.map((play) => (
        <div key={play.id} className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-bold">{play.title}</h2>
          <p className="text-gray-600">{play.author}</p>
          <p className="mt-2">{play.description}</p>
          <a 
            href={`/plays/${play.id}`}
            className="mt-4 inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Read Play
          </a>
        </div>
      ))}
    </div>
  );
};

export default PlayList;