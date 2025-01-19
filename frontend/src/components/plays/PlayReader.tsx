import { useParams } from 'react-router-dom'

const dummyPlayContent = {
  title: "Hamlet",
  author: "William Shakespeare",
  act: 1,
  scene: 1,
  content: `
    SCENE I. Elsinore. A platform before the castle.

    [Enter FRANCISCO and BERNARDO]

    BERNARDO
    Who's there?

    FRANCISCO
    Nay, answer me: stand, and unfold yourself.

    BERNARDO
    Long live the king!

    FRANCISCO
    Bernardo?

    BERNARDO
    He.
  `
}

const PlayReader = () => {
  const { id } = useParams()

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-lg shadow-md p-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">{dummyPlayContent.title}</h1>
          <p className="text-gray-600">by {dummyPlayContent.author}</p>
        </div>
        
        <div className="mb-6">
          <h2 className="text-xl font-semibold mb-2">
            Act {dummyPlayContent.act}, Scene {dummyPlayContent.scene}
          </h2>
        </div>

        <div className="prose lg:prose-xl">
          <pre className="whitespace-pre-wrap font-serif">
            {dummyPlayContent.content}
          </pre>
        </div>

        <div className="mt-8 flex justify-between">
          <button className="bg-gray-200 px-4 py-2 rounded hover:bg-gray-300">
            Previous Scene
          </button>
          <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
            Next Scene
          </button>
        </div>
      </div>
    </div>
  )
}

export default PlayReader