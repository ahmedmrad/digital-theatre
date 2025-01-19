import { Link } from 'react-router-dom'

const dummyPlays = [
  {
    id: 1,
    title: "Hamlet",
    author: "William Shakespeare",
    description: "The Tragedy of Hamlet, Prince of Denmark",
    coverImage: "https://via.placeholder.com/300x400"
  },
  {
    id: 2,
    title: "The Importance of Being Earnest",
    author: "Oscar Wilde",
    description: "A Trivial Comedy for Serious People",
    coverImage: "https://via.placeholder.com/300x400"
  },
  {
    id: 3,
    title: "A Doll's House",
    author: "Henrik Ibsen",
    description: "A three-act play in prose",
    coverImage: "https://via.placeholder.com/300x400"
  }
]

const PlayList = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Available Plays</h1>
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {dummyPlays.map((play) => (
          <div key={play.id} className="bg-white rounded-lg shadow-md overflow-hidden">
            <img 
              src={play.coverImage} 
              alt={play.title} 
              className="w-full h-48 object-cover"
            />
            <div className="p-4">
              <h2 className="text-xl font-bold mb-2">{play.title}</h2>
              <p className="text-gray-600 text-sm mb-2">by {play.author}</p>
              <p className="text-gray-700 mb-4">{play.description}</p>
              <Link 
                to={`/plays/${play.id}`}
                className="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Read Play
              </Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default PlayList